import param
import panel as pn

class Correction(param.Parameterized):

    sk = None
    row = None
    sqlkor = None
    sqlbris = None
    selsql = None
    areas = {}

    pole = ''
    kriterium = ''
    k = None
    selection = ''


    #sqlread = param.String(precedence=-1)
    user = param.String(precedence=-1)
    butt_snimikor = pn.widgets.Button(name='Save changes', button_type='primary')



    def __init__(self, **param):
        super(Correction, self).__init__(**param)

        self._kreiraj_oblast()
        self._update_view()
        self.Kor_row = pn.Column()


    rad = param.Selector(objects=["My Tables", "By Area"], default="My Tables")
    sel = param.ObjectSelector(precedence=-1)


    @param.depends('sel', watch=True)
    def _update_selection(self):
        self.selection = self.sel




    @param.depends('rad', 'user', 'selection', watch=True)
    def _update_view(self):

        if self.rad == 'By Area':
            self.param['sel'].objects = [i.parts[8] for  i in list(self.areas.keys())]
            self.param['sel'].precedence = 1

            selection = [i.parts[8] for  i in list(self.areas.keys())][0]

            self.pole = 'PATEKAOBJAVA'
            self.kriterium = """%{krit}%""".format(krit=selection)

        else:
            self.param['sel'].precedence = -1
            self.pole = 'KORISNIK'
            self.kriterium = """%{user}%""".format(user=self.user)
        print('UPDATEVIEW POLE= ', self.pole)
        print('UPDATEVIEW KRITERIUM = ', self.kriterium)

        #self._citaj_baza()



    @param.depends('pole', 'kriterium', watch=True)
    def _citaj_baza(self):
        self.Kor_row = pn.Column()
        #self.sql = self.sqlread
        print('DOJDOV CITAJ BAZA')

        print('KRITERIUM Citaj = ', self.kriterium)
        print('POLE Citaj= ', self.pole)
        if self.kriterium != '%%':

            '''
            #Za rabota
            #DATABASE_CONNECTION = 'mssql://sa:D2009eceJa!@DELLSERVER3/GK?driver=SQL Server'
            self.sql = """
            SELECT     MS_AZURIRANJE.*, KORISNIK AS Expr1
            FROM         MS_AZURIRANJE
            WHERE     (KORISNIK = 'GORANKIRANDZIS1')
            '''
            #Za doma
            DATABASE_CONNECTION = 'mssql://@USER-PC\GORANSQL/MakStat?driver=SQL Server'
            engine = create_engine(DATABASE_CONNECTION)

            self.sql = """
            SELECT     MS_AZURIRANJE.*, {pole} AS Expr1
            FROM         MS_AZURIRANJE
            WHERE     ({pole} LIKE N'{kriterium}')
            """.format(pole=self.pole, kriterium=self.kriterium)

            self.sk = pd.read_sql(self.sql, engine)

            print(self.sql)
            print(self.sk)
        else:
            self.sk = pd.DataFrame(columns=['User_ID', 'UserName', 'Action'])
            print('LEN SK = ', len(self.sk))

        #self._remove_row()
        #self._add_row()
        #return self.sk
    @param.depends('rad', 'sel', watch=True)
    def _remove_row(self):
        for i in self.Kor_row:
            widget = i

            [widget.param.unwatch(watcher) for watcher in widget.param._watchers]
            del widget

            #self.Kor_row.remove(i)
        print('IZBRISAV KOR ROW')

    @param.depends('sk', watch=True)
    def _add_row(self):
        print('DOJDOV ADD ROW')
        #self._remove_row()
        print('SELF KOR PO BRISENJE = ', self.Kor_row)
        print('OD ADD_ROW = ', self.sk)

        if len(self.sk) > 0:
            print('LEN > 0 LEN = ', len(self.sk))

            for index, self.row in self.sk.iterrows():
                rbr = pn.widgets.LiteralInput(value=self.row['RBRVNES'], disabled=True, width=50)
                #Za rabota
                #patek = pn.widgets.LiteralInput(value=self.row['PATEKAOBJAVA'].replace('U:\\KOPIJABAZI_PREDRESTARINJE\\PXWEB\\MakStat\\', ''), disabled=True, width=400)
                #Za doma
                patek = pn.widgets.LiteralInput(value=self.row['PATEKAOBJAVA'].strip().replace('C:\\inetpub\\wwwroot\\PXWeb\\Resources\\PX\\Databases\\MakStat\\', ''), disabled=True, width=400)
                datumobj = pn.widgets.DatePicker(name='Датум на објавување на веб', value=datetime.strptime(self.row['DATUMOBJAVA'], '%Y-%m-%d').date(), width=150)
                koris = pn.widgets.LiteralInput(value=self.row['KORISNIK'].strip(), disabled=True, width=250)
                datumvneseno = pn.widgets.LiteralInput(value=datetime.strftime(self.row['DATUMAZUR'], '%d-%m-%Y'), disabled=True, width=100)
                brisi = pn.widgets.Checkbox(name='За бришење')

                self.Kor_row.append(pn.Row(rbr, patek, datumobj, koris, datumvneseno, brisi))



        else:
            print('DOJDOV ADD ROW  ELSE')
            #self.Kor_row = pn.Column()

        print(self.Kor_row)
        #self.panel()
        #self.pnl[2] = self.Kor_row




    '''
    def view(self):
        return pn.Column(
            self.Kor_row,
            self.butt_snimikor,
            #self.param()
            )
    '''


    @param.depends('user')
    def view(self):
        print('DOJDOV VIEW')
        print ('USER = ', self.user)
        return pn.pane.LaTeX(('{user}'.format(user=self.user)),
                             style={'font-size': '18pt'}, width=800)
    '''
    @param.depends('action', watch=True)
    def PrevzemiPodatoci(self, event=None):
        self._remove_row()

        return pn.Column(
            #self.view,
            pn.Param(self, widgets={'rad': {'type': pn.widgets.RadioButtonGroup, 'button_type': 'success'},
                                   'sel': {'type': pn.widgets.Select, 'options': [i.parts[8] for  i in list(self.oblast1.keys())]},
                                   'action': {'type':pn.widgets.Button(button_type='primary')}},
                    ),
            self.Kor_row,
            self.butt_snimikor,
            #self.param()
        )
        '''




    def panel(self):
        print('DOJDOV PANEL')
        print('LEN KOR_ROW = ', len(self.Kor_row))
        pnl = pn.Column(
            self.view,
            pn.Param(self, widgets={'rad': {'type': pn.widgets.RadioButtonGroup, 'button_type': 'success'},
                                   'sel': {'type': pn.widgets.Select, 'options': [i.parts[8] for  i in list(self.oblast1.keys())]},
                                   'action': {'type':pn.widgets.Button(button_type='primary')}},
                    ),
            self.Kor_row,
            self.butt_snimikor,
            #self.param()
        )
        print('PNL = ', pnl)
        return pnl
    '''
    @param.depends('Kor_row')
    def replace_panel(attr, old, new):
        self.pnl[2] = self.Kor_row

    '''






    def _snimikor(event):

        print('STIGNAV VO _snimikor EVENT')
        print(event)
        #print("SELFSQL= ", self.selsql)



        '''
        #Za rabota
        # Connection example: Windows, without a DSN, using the Windows SQL Server driver
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DELLSERVER3;DATABASE=GK;UID=sa;PWD=D2009eceJa!')
        cursor = cnxn.cursor()
        cursor.execute(self.sqlkor)
        cursor.execute(self.sqlbris)
        cnxn.commit()
        '''
        print('STIGNAV PYODBC')
        #Za doma
        # Connection example: Windows, without a DSN, using the Windows SQL Server driver
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=USER-PC\GORANSQL;DATABASE=MakStat')
        cursor = cnxn.cursor()
        cursor.execute(self.sqlkor)
        cursor.execute(self.sqlbris)
        cnxn.commit()



    def _kreiraj_oblast(self):
        print('DOJDOV KREIRAJ OBLAST')
        # za rabota
        #patfolder = Path('U:/KOPIJABAZI_PREDRESTARINJE/PXWEB/MakStat/Naselenie/')

        #za doma
        patfolder = Path('C:/inetpub/wwwroot/PXWeb/Resources/PX/Databases/MakStat/Naselenie/')

        oblast1 = {}
        en = ''
        mk = ''

        for root, dirs, files in os.walk(patfolder):
            #print(files)
            for j in files:
                if j == 'Alias_mk.txt':
                    rut = Path(root)
                    patf = rut / j
                    #print(patf)

                    with open(patf, 'r', encoding='utf-8-sig') as f:
                        al = f.readlines()[0]
                        al = al.split('&nbsp')[0]
                    pp = rut.parents[0]

                    if pp not in oblast1:
                        en = rut
                        mk = en.parents[0] / al
                        oblast1.update({en:mk})
                    else:
                        en = rut
                        mk = oblast1[pp] / al
                        self.oblast1.update({en:mk})
        #print('OD Kreiraj oblasti = ', self.oblast1)
        return self.oblast1

    #print(butt_snimikor)
    butt_snimikor.on_click(_snimikor)



stage3 = Correction(user=stage1.output())
stage3.panel()