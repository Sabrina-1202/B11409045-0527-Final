# 台科大資管 Python 考試作答區

---

## 基本資料

**學號：** B11409045
**系級：** 資管系大一  
**姓名：** 蔡恬歆

---

## 一、 原始碼分析報告 (Static Analysis) (共8小題，每小題3分，總共24分)

### 1.1 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 l1 (in load_proc) |從 lib_data.txt 讀取出來的每一行原始書籍資料 |lines |
| Q2 d2 (in main) |儲存所有圖書資料的清單，每本書用 dictionary 表示 |books |
| Q3 c_res (in check) |檢查 ISBN 是否已經存在的函式 |isbn_exists|

### 1.2 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好：

- **Q1：** 變數命名不清楚，像 l1、d2、c_res 無法直接看出用途，導致閱讀與維護困難。
- **Q2：** 使用全域變數 d2 儲存資料，任何函式都可以直接修改它，容易造成資料狀態混亂。
- **Q3：** 使用 @@ 和 ## 自訂字串格式儲存資料，只要書名或資料中出現特殊符號，就可能造成解析錯誤。
- **Q4：** 沒有使用 try-except 處理檔案讀取與格式錯誤，檔案損毀或資料格式錯誤時程式可能直接崩潰。
- **Q5：** 功能全部集中在 main 裡，新增、顯示、借書、儲存邏輯混在一起，不容易測試與修改。

---

## 二、 Vibe-Coding 協作紀錄 (共6小題，每小題3分，總共18分)

請記錄你如何引導 GitHub Copilot 進行重構。
重構的要求，請根據題目卷以及你發現的 Code Smells 來進行。

### 2.1 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A： 請分析 legacy_lib.py 的程式邏輯，找出 l1、d2、c_res 分別代表什麼意思，並用表格整理原始名稱、真實用途與建議修正名稱。

Prompt B： 請將 legacy_lib.py 重構成 modern_library.py，保留原本 add 書名/ISBN/狀態、borrow ISBN、show、exit 的操作方式，但改用 class 和清楚的函式名稱撰寫。

Prompt C：請把原本 lib_data.txt 的 @@ 和 ## 自訂格式改成 books.json，並加入 try-except，處理檔案不存在、JSON 格式錯誤與使用者輸入格式錯誤。
```

### 2.2 AI 錯誤處理

1. AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？

AI 在撰寫過程中有出錯。


2. 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)

AI 一開始把 add 指令改成互動式輸入書名、ISBN、狀態，導致 test_input_data.txt 裡面的測試資料無法直接複製貼上使用。另外，AI 一開始也沒有處理 borrow 找不到 ISBN 的情況。

3. 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)

---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log

```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
  {
    "title": "XXX",
    "isbn": "XXX",
    "status": "XXX"
  }
]
```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
# 請在此處貼上 git log 內容
```

### 4.2. GitHub Repository 連結(此小題7分)

將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
# 請貼上你的 Repo 網址
```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
