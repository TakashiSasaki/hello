(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports);
        if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "clsx", "tailwind-merge"], factory);
    }
})(function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.cn = cn;
    const clsx_1 = require("clsx");
    const tailwind_merge_1 = require("tailwind-merge");
    function cn(...inputs) {
        return (0, tailwind_merge_1.twMerge)((0, clsx_1.clsx)(inputs));
    }
});
