# **NTFSのMFTレコードにおけるResident Dataの概要**

## **1. はじめに**
NTFS（New Technology File System）は、Windowsの標準的なファイルシステムであり、その管理構造の中心には **MFT（Master File Table）** がある。MFTは各ファイルのメタデータを格納するためのレコードを持ち、通常は **1KB（1024バイト）** の固定サイズで割り当てられる。  
このMFTレコード内に小さなファイルデータを直接格納する仕組みを **resident data（レジデントデータ）** と呼ぶ。本稿では、resident data の概念、格納可能なデータサイズ、およびその制限について詳細に説明する。

---

## **2. MFTレコードの構造**
1KBのMFTレコードは、以下の主要なセクションで構成される：

| セクション | 説明 | サイズの目安 |
|-----------|------|-------------|
| **固定ヘッダー** | MFTエントリの管理情報（署名、レコード番号、フラグなど） | 約56バイト |
| **属性リスト** | 各属性のエントリ（ファイル名、セキュリティ情報、データなど） | 100～300バイト |
| **Resident Data** | MFTレコード内に格納されるファイルデータ | **約700～900バイト** |
| **Non-Resident Data（該当する場合）** | ファイルデータが大きすぎる場合、MFT外部のクラスタに保存 | - |

---

## **3. Resident Dataとは**
Resident Data とは、MFTレコード内に直接保存される小さなファイルデータを指す。  
通常、NTFSはファイルサイズが小さい場合に、外部のディスククラスタを使用せず、**MFTレコード内の空き領域を活用してデータを格納** する。これにより、ディスクの断片化を抑え、読み書きのパフォーマンスを向上させることができる。

### **3.1 Resident Data の格納条件**
- **ファイルサイズがMFTレコード内の空きスペース（約700～900バイト）に収まる場合**
  - → **データはresidentとしてMFT内に格納**
- **ファイルサイズがMFTレコード内に収まらない場合**
  - → **データはnon-resident（MFT外部のクラスタ）として格納**
  
NTFSは、まずresident dataとして保存を試み、必要に応じてnon-residentへ移行する。

---

## **4. Resident Data に格納可能な最大サイズ**
### **4.1 計算方法**
MFTレコードのサイズ（通常1KB）から、固定ヘッダーおよびその他の属性データが占有する領域を差し引くことで、Resident Data に使用可能なバイト数を求めることができる。

**例：**
- **MFTレコードの総サイズ**: 1024バイト
- **固定ヘッダー（56バイト）**: -56バイト
- **ファイル名属性（~64バイト）**: -64バイト
- **セキュリティ情報（~100バイト）**: -100バイト
- **その他の属性情報（~100バイト）**: -100バイト
- **残りのスペース（Resident Data に使用可能な領域）**: **約700～900バイト**

**結論：** Resident Data に格納できるのは **最大約700～900バイト** であり、それを超えると Non-Resident になる。

### **4.2 影響要因**
- **ファイル名の長さ**  
  - ファイル名が長いほど、ファイル名属性のサイズが増加し、Resident Data に使えるスペースが減少する。
- **追加の属性情報**  
  - 圧縮、暗号化、拡張属性などが追加されると、Resident Data に使える領域が減る。
- **NTFSバージョンの違い**  
  - 一部のバージョンでは、追加のメタデータが記録されるため、Resident Data に影響を与える。

---

## **5. Resident Data の確認方法**
Windows環境で特定のファイルがresidentかどうかを確認するには、以下の方法を使用する。

### **5.1 fsutil コマンドを使用**
Windowsの `fsutil` コマンドを使うと、ファイルが resident か non-resident かを確認できる。

```powershell
fsutil file layout C:\path\to\file.txt
```
このコマンドの出力に **"Resident"** または **"Non-Resident"** の情報が含まれる。

### **5.2 $MFT を直接解析**
NTFSの **$MFT** を解析することで、resident data の詳細を取得可能。`ntfsinfo` や `MFTRCRD` などのツールを使用することで、MFTレコードの構造を詳細に確認できる。

---

## **6. まとめ**
- **Resident Data とは**: MFTレコード内に格納される小さなファイルデータのこと。
- **格納できる最大サイズ**: **約700～900バイト**（MFTレコードのメタデータ量による）。
- **ファイルが小さい場合**: Resident Data としてMFT内に保存され、高速アクセスが可能。
- **ファイルが大きい場合**: Non-Resident となり、MFT外のクラスタに保存。
- **確認方法**: `fsutil file layout` コマンドで resident / non-resident の判定が可能。

この仕組みにより、NTFSは小さなファイルを効率的に管理し、ディスクアクセスの最適化を図っている。

---

## **参考文献**
1. Microsoft Docs: [NTFS File System Overview](https://docs.microsoft.com/en-us/windows/win32/fileio/ntfs-technical-reference)
2. Brian Carrier, *File System Forensic Analysis*, Addison-Wesley, 2005.
3. Joachim Metz, *The NTFS File System*, [https://github.com/libyal](https://github.com/libyal)