# Windowsにおけるユーザー識別情報の包括的整理

本ドキュメントは、Windows環境でユーザーを識別するために利用可能な各種プロパティについて、網羅的に整理したものである。対象となるプロパティは、ユーザー（アカウント）そのものを識別する情報であり、ホストやコンピュータ自体を識別する情報（例：ホスト名やMachineGuid）とは区別する。ここでは、特に以下のプロパティについて説明する。

- **CsUserName**
- **WindowsRegisteredOwner**
- **OsRegisteredUser**
- **CsPrimaryOwnerName**

また、各プロパティが導入されたWindowsのバージョンや、NT系OSのみで利用可能であるかどうかについても言及する。

## 目次
1. [はじめに](#はじめに)
2. [ユーザー識別プロパティの概要](#ユーザー識別プロパティの概要)
   - [CsUserName](#csusername)
   - [WindowsRegisteredOwner](#windowsregisteredowner)
   - [OsRegisteredUser](#osregistereduser)
   - [CsPrimaryOwnerName](#csprimaryownername)
3. [各プロパティの詳細](#各プロパティの詳細)
   - [CsUserName](#csusername-詳細)
   - [WindowsRegisteredOwner](#windowsregisteredowner-詳細)
   - [OsRegisteredUser](#osregistereduser-詳細)
   - [CsPrimaryOwnerName](#csprimaryownername-詳細)
4. [利用可能なWindowsバージョン](#利用可能なwindowsバージョン)
5. [まとめ](#まとめ)
6. [参考文献](#参考文献)

## はじめに
Windowsでは、ユーザーアカウントに関連する複数のプロパティが存在する。これらは、システムのインストール時や初期設定時に設定される値と、ログオン時に動的に取得される値があり、状況や環境により異なる用途で利用される。本ドキュメントでは、主にユーザーを識別するために利用されるプロパティについて解説する。

## ユーザー識別プロパティの概要

### CsUserName
- **概要**: 現在ログオンしているユーザー名を示すプロパティ。  
- **特徴**: ユーザーがログオンするたびにセキュリティトークンから取得されるため、動的な値となる。  
- **用途**: 実際のログオンユーザーの識別。

### WindowsRegisteredOwner
- **概要**: Windowsのインストール時に入力された登録所有者の名前。  
- **特徴**: レジストリキー `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\RegisteredOwner` に保存される。  
- **用途**: システム設定としてのユーザー情報。手動変更も可能。

### OsRegisteredUser
- **概要**: OSが保持する登録ユーザーの情報。  
- **特徴**: WMIの `Win32_OperatingSystem` クラスから取得され、通常はWindowsRegisteredOwnerと同一の値となる。  
- **用途**: OSレベルでのユーザー登録情報として利用。

### CsPrimaryOwnerName
- **概要**: コンピューターシステムの主な所有者を示す情報。  
- **特徴**: WMIの `Win32_ComputerSystem` クラスから取得される。  
- **用途**: OEMによる出荷時の設定や、システム管理者が設定した所有者情報として利用される場合がある。

## 各プロパティの詳細

### CsUserName 詳細
- **取得方法**: PowerShellの `Get-ComputerInfo` コマンドレットで取得可能。  
- **動作**: ログオン中のユーザーのセキュリティトークンにより決定され、ユーザーが切り替われば値も変動する。  
- **利用シーン**: 現在ログオンしているユーザーの動的な識別が必要な場合に有用。

### WindowsRegisteredOwner 詳細
- **取得方法**: レジストリエディタまたは `Get-ComputerInfo` で `WindowsRegisteredOwner` プロパティとして取得可能。  
- **動作**: Windowsのインストール時に入力された登録所有者情報が反映される。  
- **バージョン**: Windows NT 3.1 から導入され、NT系列のOSで利用可能。  
- **利用シーン**: システムの初期設定情報としてのユーザー識別。

### OsRegisteredUser 詳細
- **取得方法**: WMIの `Win32_OperatingSystem` クラスを通して取得される。  
- **動作**: 通常、WindowsRegisteredOwnerと同じ値を示す。  
- **バージョン**: Windows 2000 以降に導入。  
- **利用シーン**: OSレベルの登録ユーザー情報として、ユーザーアカウント管理に利用。

### CsPrimaryOwnerName 詳細
- **取得方法**: WMIの `Win32_ComputerSystem` クラスのプロパティとして取得される。  
- **動作**: OEMが出荷時に設定する場合や、システム管理者が後から設定する場合がある。  
- **バージョン**: Windows 2000 以降に導入。  
- **利用シーン**: ハードウェアやシステムの所有者情報として、特にOEM設定の場合に重要。

## 利用可能なWindowsバージョン
- **WindowsRegisteredOwner** は、Windows NT 3.1 から導入され、NT系列のOS（Windows NT、Windows 2000、XP、Vista、7、8、10、11など）で利用可能である。  
- **OsRegisteredUser** および **CsPrimaryOwnerName** は、主に Windows 2000 以降で導入された。  
- **CsUserName** は、ログオンユーザー情報としてWindows NT以降のほぼ全てのバージョンで利用可能である。  
- これらのプロパティは、Windows 95 や Windows 3.1 などの非NT系OSでは存在しない。

## まとめ
Windowsにおいてユーザーを識別するためには、動的なログオンユーザー情報である **CsUserName** と、静的な登録情報である **WindowsRegisteredOwner**、**OsRegisteredUser**、**CsPrimaryOwnerName** の組み合わせが有効である。  
- **CsUserName** は現在のログオン状態に応じて変化するが、実際の利用者の識別には最適。  
- **WindowsRegisteredOwner** と **OsRegisteredUser** は、インストール時に設定されたユーザー情報であり、基本的には変更されない（ただし、レジストリでの手動変更が可能）。  
- **CsPrimaryOwnerName** は、システム管理者やOEMによって設定される所有者情報として利用される。  
これらのプロパティは、Windows NT系列以降のOSにおいて提供され、NT系OSにおいてユーザー識別情報として標準的に利用される。

## 参考文献
- Microsoft Learn: [Win32_ComputerSystem class](https://learn.microsoft.com/ja-jp/windows/win32/cimwin32prov/win32-computersystem)
- Microsoft Learn: [Win32_OperatingSystem class](https://learn.microsoft.com/ja-jp/windows/win32/cimwin32prov/win32-operatingsystem)
- Registry の情報: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\RegisteredOwner`
- 各種 PowerShell コマンドレットのドキュメント

