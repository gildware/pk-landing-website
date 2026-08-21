/**
 * Browser Meta Pixel helpers. The base snippet (init + PageView) lives in BaseLayout.
 * This module fires page-level extra events once, and WhatsApp click intent.
 */
import type { MetaPixelPageEvent } from '@/utils/metaPixelPage';

type TrackOptions = { eventID?: string };

const STANDARD_EVENTS = new Set([
  'PageView',
  'ViewContent',
  'Lead',
  'Contact',
  'CompleteRegistration',
  'Schedule',
  'Search',
  'AddToCart',
  'InitiateCheckout',
  'Purchase',
  'Subscribe',
]);

const firedOnce = new Set<string>();
let whatsAppClicksBound = false;
let lastWhatsAppKey = '';
let lastWhatsAppAt = 0;

function fbqReady(): boolean {
  return typeof window.fbq === 'function';
}

function track(
  event: string,
  params?: Record<string, unknown>,
  options?: TrackOptions,
  onceKey?: string,
) {
  if (!fbqReady()) return;
  if (onceKey) {
    if (firedOnce.has(onceKey)) return;
    firedOnce.add(onceKey);
  }

  const method = STANDARD_EVENTS.has(event) ? 'track' : 'trackCustom';
  const payload = params ?? {};
  if (options?.eventID) {
    window.fbq!(method, event, payload, { eventID: options.eventID });
  } else {
    window.fbq!(method, event, payload);
  }
}

function readPageEvent(): MetaPixelPageEvent | null {
  const el = document.getElementById('pk-meta-page-event');
  if (!el?.textContent?.trim()) return null;
  try {
    return JSON.parse(el.textContent) as MetaPixelPageEvent;
  } catch {
    return null;
  }
}

function fireConfiguredPageEvent() {
  const pageEvent = readPageEvent();
  if (!pageEvent?.event) return;

  const params: Record<string, unknown> = {
    content_name: pageEvent.contentName,
    content_type: pageEvent.contentType,
  };
  if (pageEvent.contentIds?.length) params.content_ids = pageEvent.contentIds;
  if (pageEvent.contentCategory) params.content_category = pageEvent.contentCategory;

  track(pageEvent.event, params, undefined, `${pageEvent.event}:${window.location.pathname}`);
}

function isWhatsAppUrl(href: string | null | undefined): boolean {
  if (!href) return false;
  try {
    const url = new URL(href, window.location.origin);
    const host = url.hostname.replace(/^www\./, '');
    return host === 'wa.me' || host === 'api.whatsapp.com' || host.endsWith('whatsapp.com');
  } catch {
    return /wa\.me|whatsapp\.com/i.test(href);
  }
}

function trackWhatsAppClick(source = 'link') {
  const key = `${source}:${window.location.pathname}`;
  const now = Date.now();
  // Ignore duplicate click/keyboard handlers on the same control (~same moment).
  if (key === lastWhatsAppKey && now - lastWhatsAppAt < 400) return;
  lastWhatsAppKey = key;
  lastWhatsAppAt = now;

  track('WhatsAppClick', {
    content_name: document.title,
    content_category: window.location.pathname,
    source,
  });
}

function bindWhatsAppClicks() {
  if (whatsAppClicksBound) return;
  whatsAppClicksBound = true;

  document.addEventListener(
    'click',
    (event) => {
      const target = event.target;
      if (!(target instanceof Element)) return;
      const link = target.closest('a[href]');
      if (!link) return;
      if (!isWhatsAppUrl(link.getAttribute('href'))) return;
      trackWhatsAppClick('link');
    },
    true,
  );
}

function pkTrackMeta(event: string, params?: Record<string, unknown>, options?: TrackOptions) {
  if (event === 'Lead') {
    const onceKey = options?.eventID ? `Lead:${options.eventID}` : `Lead:${window.location.pathname}`;
    track(event, params, options, onceKey);
    return;
  }
  if (event === 'WhatsAppClick') {
    trackWhatsAppClick(typeof params?.source === 'string' ? params.source : 'script');
    return;
  }
  track(event, params, options);
}

window.pkTrackMeta = pkTrackMeta;
fireConfiguredPageEvent();
bindWhatsAppClicks();
