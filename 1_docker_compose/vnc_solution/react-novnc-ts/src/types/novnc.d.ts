declare module "@novnc/novnc/lib/rfb" {
  export default class RFB {
    constructor(
      target: HTMLElement,
      url: string,
      options?: {
        credentials?: {
          target?: string;
          username?: string;
          password?: string;
        };
      }
    );

    viewOnly: boolean;
    scaleViewport: boolean;
    background: string;

    disconnect(): void;
  }
}
