var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports);
        if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "react/jsx-runtime", "react", "@/lib/utils"], factory);
    }
})(function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.CardContent = exports.CardDescription = exports.CardTitle = exports.CardFooter = exports.CardHeader = exports.Card = void 0;
    const jsx_runtime_1 = require("react/jsx-runtime");
    const React = __importStar(require("react"));
    const utils_1 = require("@/lib/utils");
    const Card = React.forwardRef((_a, ref) => {
        var { className } = _a, props = __rest(_a, ["className"]);
        return ((0, jsx_runtime_1.jsx)("div", Object.assign({ ref: ref, className: (0, utils_1.cn)("rounded-lg border bg-card text-card-foreground shadow-sm", className) }, props)));
    });
    exports.Card = Card;
    Card.displayName = "Card";
    const CardHeader = React.forwardRef((_a, ref) => {
        var { className } = _a, props = __rest(_a, ["className"]);
        return ((0, jsx_runtime_1.jsx)("div", Object.assign({ ref: ref, className: (0, utils_1.cn)("flex flex-col space-y-1.5 p-6", className) }, props)));
    });
    exports.CardHeader = CardHeader;
    CardHeader.displayName = "CardHeader";
    const CardTitle = React.forwardRef((_a, ref) => {
        var { className } = _a, props = __rest(_a, ["className"]);
        return ((0, jsx_runtime_1.jsx)("h3", Object.assign({ ref: ref, className: (0, utils_1.cn)("text-2xl font-semibold leading-none tracking-tight", className) }, props)));
    });
    exports.CardTitle = CardTitle;
    CardTitle.displayName = "CardTitle";
    const CardDescription = React.forwardRef((_a, ref) => {
        var { className } = _a, props = __rest(_a, ["className"]);
        return ((0, jsx_runtime_1.jsx)("p", Object.assign({ ref: ref, className: (0, utils_1.cn)("text-sm text-muted-foreground", className) }, props)));
    });
    exports.CardDescription = CardDescription;
    CardDescription.displayName = "CardDescription";
    const CardContent = React.forwardRef((_a, ref) => {
        var { className } = _a, props = __rest(_a, ["className"]);
        return ((0, jsx_runtime_1.jsx)("div", Object.assign({ ref: ref, className: (0, utils_1.cn)("p-6 pt-0", className) }, props)));
    });
    exports.CardContent = CardContent;
    CardContent.displayName = "CardContent";
    const CardFooter = React.forwardRef((_a, ref) => {
        var { className } = _a, props = __rest(_a, ["className"]);
        return ((0, jsx_runtime_1.jsx)("div", Object.assign({ ref: ref, className: (0, utils_1.cn)("flex items-center p-6 pt-0", className) }, props)));
    });
    exports.CardFooter = CardFooter;
    CardFooter.displayName = "CardFooter";
});
