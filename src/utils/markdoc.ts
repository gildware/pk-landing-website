import Markdoc from '@markdoc/markdoc';

type BodyLoader = () => Promise<{ node: unknown } | null | undefined>;

export async function renderMarkdocHtml(bodyLoader: BodyLoader): Promise<string | null> {
  try {
    const result = await bodyLoader();
    if (!result?.node) return null;
    const content = Markdoc.transform(result.node as Parameters<typeof Markdoc.transform>[0]);
    return Markdoc.renderers.html(content);
  } catch {
    return null;
  }
}
