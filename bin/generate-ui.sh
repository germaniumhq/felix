cd $(readlink -f "$(dirname "$0")/..")

pyside2-uic ui/AddBranchDialog.ui > germanium_build_monitor/ui/AddBranchDialog.py
pyside2-uic ui/MainWindow.ui > germanium_build_monitor/ui/MainWindow.py
pyside2-uic ui/AddJobDialog.ui > germanium_build_monitor/ui/AddJobDialog.py
pyside2-uic ui/JobBranchView.ui > germanium_build_monitor/ui/JobBranchView.py
pyside2-uic ui/SystrayWindow.ui > germanium_build_monitor/ui/SystrayWindow.py

