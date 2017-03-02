from ScopeFoundry import BaseApp
from ScopeFoundry.ndarray_interactive import ArrayLQ_QTableModel
from qtpy import QtWidgets

import logging
logging.basicConfig(level='DEBUG')

class LQArrayTestApp(BaseApp):
    
    name = 'LQArrayTestApp'
    
    def __init__(self,argv):
        BaseApp.__init__(self,argv)
        
        self.settings.New('test_array', dtype=float, array=True,  ro=False, fmt="%1.2f",
                  initial=[[147, 111 , 100]])#,[208, 8 , 100],[218, 45 , 100],[345, 1500 , 100,],[517, 8 , 100],[772, 300, 100]])

        self.test_array_model = ArrayLQ_QTableModel(
            self.settings.test_array, 
            col_names=['Center','FWHM', 'Amplitude'])
        
        self.ui = QtWidgets.QWidget()
        self.ui.setLayout(QtWidgets.QVBoxLayout())
        
        self.tableView1 = QtWidgets.QTableView()
        self.tableView1.setModel(self.test_array_model)
        self.ui.layout().addWidget(self.tableView1)

        self.tableView2 = QtWidgets.QTableView()
        self.tableView2.setModel(self.test_array_model)
        self.ui.layout().addWidget(self.tableView2)


        self.test_array_model3 = ArrayLQ_QTableModel(self.settings.test_array )
        self.tableView3 = QtWidgets.QTableView()
        self.tableView3.horizontalHeader().hide()
        self.tableView3.setModel(self.test_array_model3)
        self.ui.layout().addWidget(self.tableView3)

        self.settings.New('test_array4', dtype=float, array=True,  ro=False, fmt="%1.2f",
                  initial=[1, 2 , 3])
        self.test_array_model4 = ArrayLQ_QTableModel(self.settings.test_array4 )
        self.tableView4 = QtWidgets.QTableView()
        self.tableView4.setModel(self.test_array_model4)
        self.ui.layout().addWidget(self.tableView4)

        self.test_array_model5 = ArrayLQ_QTableModel(self.settings.test_array4 , transpose=True)
        self.tableView5 = QtWidgets.QTableView()
        self.tableView5.setModel(self.test_array_model5)
        self.ui.layout().addWidget(self.tableView5)

        for dtype in [str, bool, int]:
            lq_name = 'test_array_{}'.format(dtype.__name__)
            lq = self.settings.New(lq_name, dtype=dtype, array=True,  ro=False,
                      initial=[0,1,"20",0])

            tableModel = ArrayLQ_QTableModel(lq, row_names= [dtype.__name__,], fmt=lq.fmt, transpose=True) 
            tableView = QtWidgets.QTableView()
            tableView.setModel(tableModel)
            self.ui.layout().addWidget(tableView)
            
        # Bool doesnot work yet, int does not round

        self.ui.show()
        self.console_widget.show()
        
        
if __name__ == '__main__':
    app = LQArrayTestApp([])
    app.exec_()