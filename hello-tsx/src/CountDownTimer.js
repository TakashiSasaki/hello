(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports);
        if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "react/jsx-runtime", "react", "@/components/ui/button", "@/components/ui/input", "@/components/ui/card"], factory);
    }
})(function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    const jsx_runtime_1 = require("react/jsx-runtime");
    const react_1 = require("react");
    const button_1 = require("@/components/ui/button");
    const input_1 = require("@/components/ui/input");
    const card_1 = require("@/components/ui/card");
    // コンポーネントの定義
    function CountDownTimer() {
        const [time, setTime] = (0, react_1.useState)(300);
        const [isRunning, setIsRunning] = (0, react_1.useState)(false);
        const [inputTime, setInputTime] = (0, react_1.useState)('5');
        (0, react_1.useEffect)(() => {
            let interval = null;
            if (isRunning && time > 0) {
                interval = setInterval(() => {
                    setTime((prevTime) => prevTime - 1);
                }, 1000);
            }
            else if (time === 0) {
                setIsRunning(false);
            }
            return () => {
                if (interval)
                    clearInterval(interval);
            };
        }, [isRunning, time]);
        const formatTime = (seconds) => {
            const minutes = Math.floor(seconds / 60);
            const remainingSeconds = seconds % 60;
            return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
        };
        const handleStart = () => setIsRunning(true);
        const handlePause = () => setIsRunning(false);
        const handleReset = () => {
            setIsRunning(false);
            setTime(parseInt(inputTime) * 60);
        };
        const handleInputChange = (e) => {
            const value = e.target.value;
            setInputTime(value);
            if (value && !isNaN(parseInt(value))) {
                setTime(parseInt(value) * 60);
            }
        };
        return ((0, jsx_runtime_1.jsxs)(card_1.Card, { className: "w-full max-w-md mx-auto", children: [(0, jsx_runtime_1.jsx)(card_1.CardHeader, { children: (0, jsx_runtime_1.jsx)(card_1.CardTitle, { className: "text-center", children: "\u30AB\u30A6\u30F3\u30C8\u30C0\u30A6\u30F3\u30BF\u30A4\u30DE\u30FC" }) }), (0, jsx_runtime_1.jsxs)(card_1.CardContent, { className: "flex flex-col items-center space-y-4", children: [(0, jsx_runtime_1.jsx)("div", { className: "text-6xl font-bold tabular-nums", children: formatTime(time) }), (0, jsx_runtime_1.jsxs)("div", { className: "flex space-x-2", children: [(0, jsx_runtime_1.jsx)(button_1.Button, { onClick: handleStart, disabled: isRunning, children: "\u958B\u59CB" }), (0, jsx_runtime_1.jsx)(button_1.Button, { onClick: handlePause, disabled: !isRunning, children: "\u4E00\u6642\u505C\u6B62" }), (0, jsx_runtime_1.jsx)(button_1.Button, { onClick: handleReset, children: "\u30EA\u30BB\u30C3\u30C8" })] }), (0, jsx_runtime_1.jsxs)("div", { className: "flex items-center space-x-2", children: [(0, jsx_runtime_1.jsx)(input_1.Input, { type: "number", value: inputTime, onChange: handleInputChange, className: "w-20", min: "1" }), (0, jsx_runtime_1.jsx)("span", { children: "\u5206" })] })] })] }));
    }
    (function (factory) {
        if (typeof module === "object" && typeof module.exports === "object") {
            module.exports = factory(require("react"));
        }
        else if (typeof define === "function" && define.amd) {
            define(["react"], factory);
        }
        else {
            const Component = factory(window.React);
            if (typeof window !== "undefined") {
                window.Component = Component;
            }
        }
    })(function (React) {
        return CountDownTimer;
    });
});
