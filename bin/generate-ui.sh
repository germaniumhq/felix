cd $(readlink -f "$(dirname "$0")/..")

pyside2-uic ui/AddBranchDialog.ui > germanium_build_monitor/ui/Ui_AddBranchDialog.py
pyside2-uic ui/MainWindow.ui > germanium_build_monitor/ui/Ui_MainWindow.py
pyside2-uic ui/AddJobDialog.ui > germanium_build_monitor/ui/Ui_AddJobDialog.py
pyside2-uic ui/JobBranchView.ui > germanium_build_monitor/ui/Ui_JobBranchView.py

pyside2-uic ui/NewStartFrame.ui > germanium_build_monitor/ui/Ui_NewStartFrame.py
