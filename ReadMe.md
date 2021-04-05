# Log Automation Studio Upgrades

## Usage
On Windows, run (LogAsUpgrades.exe)[https://github.com/tmatijevich/LogAsUpgrades/releases/download/0.0.1/LogAsUpgrades.exe]. This will search for and list all Automation Studio upgrades installed.

Alternatively with Python, clone this repository and run:

```
> python AsLogUpgrades.py
```

### Example

```
================================================================================
B&R Automation Runtime Upgrades
================================================================================

Type    |Name                    |Version     |AS Version  |File                                |Date Installed          
--------+------------------------+------------+------------+------------------------------------+------------------------
AR      |AR000                   |4.73.2.2    |4.7.1.1     |AS4_AR_B0473_AR000.exe              |2020-11-25 at 13:35:20
AR      |APC9xxS                 |4.73.2.2    |4.7.1.1     |AS4_AR_B0473_APC9xxS.exe            |2020-12-02 at 12:37:34
AR      |APC9xxS                 |4.73.3.1    |4.7.1.1     |AS4_AR_C0473_APC9xxS.exe            |2020-12-17 at 10:25:49
AR      |APC9xx                  |4.73.3.1    |4.7.1.1     |AS4_AR_C0473_APC9xx.exe             |2020-12-17 at 10:31:07
AR      |X20CP1584               |4.73.3.1    |4.7.1.1     |AS4_AR_C0473_X20CP1584.exe          |2020-12-21 at 15:44:58
AR      |X20CP1585               |4.73.3.1    |4.7.1.1     |AS4_AR_C0473_X20CP1585.exe          |2020-12-21 at 15:45:03
AR      |X20CP1586               |4.73.3.1    |4.7.1.1     |AS4_AR_C0473_X20CP1586.exe          |2020-12-21 at 15:45:08
AR      |X20CP1583               |4.73.3.1    |4.7.1.1     |AS4_AR_C0473_X20CP1583.exe          |2021-02-01 at 16:32:46
AR      |APC9xxS                 |4.83.2.3    |4.8.1.1     |AS4_AR_B0483_APC9xxS.exe            |2021-02-24 at 10:04:59
AR      |APC9xxS                 |4.53.2.1    |4.5.1.1     |AS4_AR_B0453_APC9xxS.exe            |2021-03-01 at 14:40:14

================================================================================
B&R Automation Studio 4.7 Upgrades
================================================================================

Type    |Name                    |Version     |AS Version  |File                                |Date Installed          
--------+------------------------+------------+------------+------------------------------------+------------------------
AS      |4.7.5.60 SP             |4.7.5.60    |4.7.0       |AS4_AS_4.7.5.60_SP.exe              |2020-11-25 at 13:03:20
HW      |8F1I01.AA66.xxxx-1      |1.0.0.1     |4.7.2       |AS4_HW_8F1I01.AA66.xxxx-1.exe       |2020-11-25 at 13:05:42
HW      |8F1I01.AB2B.xxxx-1      |1.0.0.1     |4.7.2       |AS4_HW_8F1I01.AB2B.xxxx-1.exe       |2020-11-25 at 13:05:43
HW      |8F1I01.BA2B.xxxx-1      |1.0.0.1     |4.7.2       |AS4_HW_8F1I01.BA2B.xxxx-1.exe       |2020-11-25 at 13:05:43
HW      |8F1I01.BB4B.xxxx-1      |1.0.0.1     |4.7.2       |AS4_HW_8F1I01.BB4B.xxxx-1.exe       |2020-11-25 at 13:05:44
HW      |5LS182.6-2              |1.7.0.0     |4.0.11      |AS4_HW_5LS182.6-2.exe               |2020-12-02 at 11:31:44
HW      |5PC910.SX05-00          |2.0.3.0     |4.0.14      |AS4_HW_5PC910.SX05-00.exe           |2020-12-02 at 11:31:46
HW      |5AC901.IPLK-00          |1.7.0.0     |4.1.4       |AS4_HW_5AC901.IPLK-00.exe           |2020-12-02 at 11:31:47
DT      |8MSA2S.R0-I6            |1.0.0.0     |4.0.11      |AS4_DT_8MSA2S.R0-I6.exe             |2021-02-01 at 18:10:44
HW      |5PC910.SX02-00          |2.0.3.0     |4.0.14      |AS4_HW_5PC910.SX02-00.exe           |2021-03-01 at 14:34:02
HW      |X20BC1083               |2.7.0.0     |4.0.11      |AS4_HW_X20BC1083.exe                |2021-03-01 at 14:34:09
HW      |X20DS1319               |1.4.0.0     |4.0.11      |AS4_HW_X20DS1319.exe                |2021-03-01 at 14:34:18

================================================================================
B&R Automation Studio 4.9 Upgrades
================================================================================

Type    |Name                    |Version     |AS Version  |File                                |Date Installed          
--------+------------------------+------------+------------+------------------------------------+------------------------
HW      |5ACPCE.FMIO-K01         |1.0.6.0     |4.2.10      |AS4_HW_5ACPCE.FMIO-K01.exe          |2021-04-05 at 09:09:48
```

## Build 

### Pre-requisites
- [Python 3](https://www.python.org/downloads/)
- [pyinstaller](https://pypi.org/project/pyinstaller/)

### Execute build

```
> workon <env>

(<env>) > pip install --upgrade pyinstaller
(<env>) > pyinstaller AsLogUpgrades.py -F
```

- See [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/) for creating new python environments
- `-F` package into a single file
