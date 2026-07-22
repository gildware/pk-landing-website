/** Canonical SEO-friendly booking page path. */
export const BOOK_PATH = '/book-a-home-service';

/** Shown after a successful online booking submit. */
export const BOOK_THANK_YOU_PATH = '/book-a-home-service/thank-you';

/** Canonical partner application page path. */
export const PARTNER_PATH = '/become-a-partner';

/** Shown after a successful partner application submit. */
export const PARTNER_THANK_YOU_PATH = '/become-a-partner/thank-you';

/** sessionStorage keys used to pass WhatsApp message text to thank-you pages. */
export const BOOKING_WA_STORAGE_KEY = 'pk-booking-wa';
export const PARTNER_WA_STORAGE_KEY = 'pk-partner-wa';

export interface BookingSite {
  businessName: string;
  phone: string;
  whatsapp: string;
  email: string;
  bookingUrl: string;
  userPlayStoreUrl: string;
  userAppStoreUrl: string;
  providerPlayStoreUrl?: string;
  providerAppStoreUrl?: string;
}

export interface BookUrlParams {
  /** Service page slug or parent category slug (e.g. carpentry-installation, plumbing). */
  service?: string;
  /** District slug (e.g. budgam) or free-text area hint. */
  area?: string;
  /** Optional details prefill for the message field. */
  details?: string;
}

/** Build `/book-a-home-service` with optional service / area / details query params. */
export function bookUrl(params: BookUrlParams = {}): string {
  const q = new URLSearchParams();
  if (params.service?.trim()) q.set('service', params.service.trim());
  if (params.area?.trim()) q.set('area', params.area.trim());
  if (params.details?.trim()) q.set('details', params.details.trim());
  const qs = q.toString();
  return qs ? `${BOOK_PATH}?${qs}` : BOOK_PATH;
}

export function partnerWhatsAppMessage() {
  return "Hi Panun Kaergar, I'd like to join as a service partner in Srinagar. Please help me get started.";
}

export function whatsappDigits(whatsapp: string) {
  return whatsapp.replace(/\D/g, '');
}

export function whatsappHref(whatsapp: string, message: string) {
  return `https://wa.me/${whatsappDigits(whatsapp)}?text=${encodeURIComponent(message)}`;
}

export function buildBookingWhatsAppMessage(data: {
  name: string;
  phone: string;
  service: string;
  area: string;
  preferredDate?: string;
  message?: string;
}) {
  const lines = [
    `Hello ${data.name ? '' : 'Panun Kaergar'}, I'd like to book a home service.`,
    data.name ? `Name: ${data.name}` : '',
    `Phone: ${data.phone}`,
    `Service: ${data.service}`,
    `Area: ${data.area}`,
    data.preferredDate ? `Preferred date/time: ${data.preferredDate}` : '',
    data.message ? `Details: ${data.message}` : '',
    '',
    'Sent via panunkaergar.com',
  ].filter(Boolean);
  return lines.join('\n');
}

export function generalWhatsAppMessage() {
  return "Hi Panun Kaergar, I'd like to book a home service in Kashmir. Please help.";
}
