/// <reference path="../.astro/types.d.ts" />

export {};

declare global {
  interface Window {
    fbq?: (...args: unknown[]) => void;
    _fbq?: unknown;
    pkTrackMeta?: (
      event: string,
      params?: Record<string, unknown>,
      options?: { eventID?: string },
    ) => void;
  }
}
