# DreamKnot
DreamKnot 是一個基於Python的進階程式語言

⚠️DreamKnot還沒完成，目前是草稿狀態，造成不便，敬請見諒⚠️

# 更多語言
[English](../README.md) | 台灣中文 

# 告訴我們你的夢想
填寫[此表單](https://forms.gle/XWxE8HftuyitmGeA7)來讓我們知道你想要什麼樣的語法，我們會儘量依照大家的填表的方式設計此語言

# 分析報告
尚無分析報告，正在等待表單回應。

# 我們幫你多做一點
我們希望讓任何人都能輕鬆進行程式設計。

我們相信您應該少花點時間思考如何編碼，多花點時間發揮創意。
所以請相信我們，我們將使這一切變得簡單。

對於經驗豐富的程式設計師來說，有些語法可能看起來很奇怪，但實際上非常簡單，只需看下面的例子。

# 基礎知識
## 語法
DreamKnot 沒有嚴格的語法規則。 （至少目前是如此）

每行結尾不用有結尾符號
```dk
print hello world
```

## 命名
您可以使用任何unicode字元來命名您的變數。
```dk
myVar = 0
myVar2 = True
myVar3 = "hello"
```
其中包括數字。
```dk
3 = 2
print（1 + 1 === 3）//true
```

## 輸出
DreamKnot 使用 `print` 來輸出。

列印行後面的所有內容都將列印
```dk
print "hello world"
```
您也可以使用括號。
```dk
print("hello world")
```

## 變數
變數名稱位於 `=` 符號前面，值位於 `=` 符號後面

您可以不指定變數型態。
```dk
variable = 0
```
或指定
```dk
int variable = 0
```
**注意:** 類型在 DreamKnot 中不起作用，但它會讓一些人更好過一點。

## 輸入
DreamKnot 使用 `input` 來輸入。

使用變數儲存輸入
```dk
myInput = input
```

您也可以指定輸入的類型
```dk
myInput = input int
```

# 進階
## 常數
常數有三種。
常數可以被編輯，但不能重新指定。
```dk
const 名稱 = "KS"
名.pop()
```

常常數無論如何都不能改變。
```dk
const const 名稱 = "KS"
```

常常常數無論如何都不能改變，而且它是全域指定的。
```dk
const const const pi = "3.14" 複製程式碼
```
**注意:** 使用"const const const"非常危險，因為會永久影響所有檔案的執行。

# 貢獻
請參閱[CONTRIBUTE.md(英文)](/CONTRIBUTE.md)