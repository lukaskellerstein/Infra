import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./index.css";

console.log("URL");
console.log(window.location.href);
console.log("BASE_PATH");
console.log(import.meta.env.BASE_PATH);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    {/* <BrowserRouter basename={import.meta.env.BASE_PATH || "/"}> */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
