# NTU_sign_in_and_out
台大教職員/計畫助理自動簽到退<br/><br/>
使用 Selenium 自動化測試工具與 Python 實作簽到腳本<br/>
Webdriver 預設為 Chrome，放在 "C:\temp\chrome"

參考構想來自: https://github.com/Winedays/ntu_auto_signing

# Requirements
Python 3.6.15<br/>
Selenium 3.141.0

# Getting started
修改 config.ini 檔案設定<br/>
UserName 後方輸入帳號<br/>
Password 後方輸入密碼

# Note
預設 Python 檔與 Config 放在同目錄下<br/>
可透過 Pyinstaller 完成簡易打包成執行檔<br/>
再依據作業系統安排自動執行時程
