cd $(readlink -f "$(dirname "$0")/..")

#pyside2-uic ui/MainWindow.ui > germanium_build_monitor/ui/Ui_MainWindow.py

pyside2-uic ui/AddServerDialog.ui > germanium_build_monitor/ui/Ui_AddServerDialog.py
#pyside2-uic ui/AddBranchDialog.ui > germanium_build_monitor/ui/Ui_AddBranchDialog.py
#pyside2-uic ui/AddJobDialog.ui > germanium_build_monitor/ui/Ui_AddJobDialog.py
#pyside2-uic ui/AddFolderDialog.ui > germanium_build_monitor/ui/Ui_AddFolderDialog.py
pyside2-uic ui/AddJobsFromServer.ui > germanium_build_monitor/ui/Ui_AddJobsFromServerDialog.py
pyside2-uic ui/MainDialog.ui > germanium_build_monitor/ui/Ui_MainDialog.py

#pyside2-uic ui/JobBranchView.ui > germanium_build_monitor/ui/Ui_JobBranchView.py

pyside2-uic ui/NewStartFrame.ui > germanium_build_monitor/ui/Ui_NewStartFrame.py
pyside2-uic ui/ServersOverviewFrame.ui > germanium_build_monitor/ui/Ui_ServersOverviewFrame.py
pyside2-uic ui/SelectJobsFrame.ui > germanium_build_monitor/ui/Ui_SelectJobsFrame.py
pyside2-uic ui/LoadingFrame.ui > germanium_build_monitor/ui/Ui_LoadingFrame.py
#pyside2-uic ui/NoSelectionFrame.ui > germanium_build_monitor/ui/Ui_NoSelectionFrame.py
