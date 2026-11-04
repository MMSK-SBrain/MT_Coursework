/** @type {import('next').NextConfig} */
const nextConfig = {
  // Workspace packages ship TypeScript source.
  transpilePackages: ["@cg/core", "@cg/harness", "@cg/exports"],
  eslint: { ignoreDuringBuilds: true },
  serverExternalPackages: ["postgres", "pptxgenjs", "docx"],
  webpack(config) {
    // Workspace packages import "./model.js" that is really model.ts.
    config.resolve.extensionAlias = { ".js": [".ts", ".tsx", ".js"] };
    // @cg/harness builds a runtime path with `new URL("../../../courses", import.meta.url)` (the worked-example
    // courses). Webpack would treat that as an asset import of a directory; keep it a plain runtime URL.
    // Set CG_COURSES_DIR in deployments so the harness finds the examples.
    config.module.rules.push({ test: /[\\/]packages[\\/]harness[\\/]/, parser: { url: false } });
    return config;
  },
};
export default nextConfig;
