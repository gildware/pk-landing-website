/** Page-level Meta Pixel event passed from Astro layouts into the client tracker. */
export type MetaPixelPageEvent = {
  event: 'ServiceView' | 'ViewContent';
  contentName: string;
  contentIds?: string[];
  contentType?: string;
  contentCategory?: string;
};
