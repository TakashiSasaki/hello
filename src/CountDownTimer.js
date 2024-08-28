"use strict";
"use client";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = Component;
const react_1 = require("react");
const button_1 = require("@/components/ui/button");
const input_1 = require("@/components/ui/input");
const card_1 = require("@/components/ui/card");
function Component() {
    const [time, setTime] = (0, react_1.useState)(300); // 5分（300秒）をデフォルトに設定
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
    return (<card_1.Card className="w-full max-w-md mx-auto">
      <card_1.CardHeader>
        <card_1.CardTitle className="text-center">カウントダウンタイマー</card_1.CardTitle>
      </card_1.CardHeader>
      <card_1.CardContent className="flex flex-col items-center space-y-4">
        <div className="text-6xl font-bold tabular-nums">
          {formatTime(time)}
        </div>
        <div className="flex space-x-2">
          <button_1.Button onClick={handleStart} disabled={isRunning}>
            開始
          </button_1.Button>
          <button_1.Button onClick={handlePause} disabled={!isRunning}>
            一時停止
          </button_1.Button>
          <button_1.Button onClick={handleReset}>
            リセット
          </button_1.Button>
        </div>
        <div className="flex items-center space-x-2">
          <input_1.Input type="number" value={inputTime} onChange={handleInputChange} className="w-20" min="1"/>
          <span>分</span>
        </div>
      </card_1.CardContent>
    </card_1.Card>);
}
