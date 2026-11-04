import type { Metadata } from "next";
import type { ReactNode } from "react";
import { PaywallProvider } from "@/components/paywall";
import { SiteFeedback } from "@/components/site-feedback";
import "./globals.css";
import "./app.css";

export const metadata: Metadata = {
  title: "Course Generator",
  description: "Design industry-relevant courses from a handout or module list, all the way to hour-wise lesson plans.",
};

// Sets data-theme before paint from the saved choice (auto follows the system).
const themeScript = `try{var t=localStorage.getItem("cg-theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}catch(e){}`;

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        {/* eslint-disable-next-line @next/next/no-page-custom-font */}
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Source+Sans+3:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"
        />
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body>
        <PaywallProvider>
          {children}
          <SiteFeedback />
        </PaywallProvider>
      </body>
    </html>
  );
}
