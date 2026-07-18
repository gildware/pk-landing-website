/** Canonical SEO-friendly booking page path. */
export const BOOK_PATH = '/book-a-home-service';

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
  return "Hi Panun Kaergar, I'd like to book a home service in Srinagar. Please help.";
}
