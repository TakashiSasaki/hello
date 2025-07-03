import React, { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

// コンポーネントの定義
function CountDownTimer() {
    const [time, setTime] = useState(300);
    const [isRunning, setIsRunning] = useState(false);
    const [inputTime, setInputTime] = useState('5');

    useEffect(() => {
        let interval: NodeJS.Timeout | null = null;
        if (isRunning && time > 0) {
            interval = setInterval(() => {
                setTime((prevTime) => prevTime - 1);
            }, 1000);
        } else if (time === 0) {
            setIsRunning(false);
        }
        return () => {
            if (interval) clearInterval(interval);
        };
    }, [isRunning, time]);

    const formatTime = (seconds: number) => {
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

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        setInputTime(value);
        if (value && !isNaN(parseInt(value))) {
            setTime(parseInt(value) * 60);
        }
    };

    return (
        <Card className="w-full max-w-md mx-auto">
            <CardHeader>
                <CardTitle className="text-center">カウントダウンタイマー</CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col items-center space-y-4">
                <div className="text-6xl font-bold tabular-nums">
                    {formatTime(time)}
                </div>
                <div className="flex space-x-2">
                    <Button onClick={handleStart} disabled={isRunning}>
                        開始
                    </Button>
                    <Button onClick={handlePause} disabled={!isRunning}>
                        一時停止
                    </Button>
                    <Button onClick={handleReset}>
                        リセット
                    </Button>
                </div>
                <div className="flex items-center space-x-2">
                    <Input
                        type="number"
                        value={inputTime}
                        onChange={handleInputChange}
                        className="w-20"
                        min="1"
                    />
                    <span>分</span>
                </div>
            </CardContent>
        </Card>
    );
}

// 型定義の追加
declare var define: {
  (deps: string[], factory: (...modules: any[]) => any): void;
  amd: boolean;
};

declare global {
  interface Window {
      Component: any;
  }
}

(function (factory: any) {
  if (typeof module === "object" && typeof module.exports === "object") {
      module.exports = factory(require("react"));
  } else if (typeof define === "function" && define.amd) {
      define(["react"], factory);
  } else {
      const Component = factory(window.React);
      if (typeof window !== "undefined") {
          window.Component = Component;
      }
  }
})(function (React: any) {
  return CountDownTimer;
});