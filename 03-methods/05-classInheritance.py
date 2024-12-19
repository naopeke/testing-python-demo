class Device:
    #デバイス名（name）、接続方法（connected_by）、および接続状態（connected）を初期化
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    #デバイスの情報を文字列形式で返す
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by}) "
    
    #デバイスを切断するメソッドで、connectedをFalseに設定
    def disconnect(self):
        self.connected = False
        print("Disconnected.")

printer = Device("Printer", "USB")
print(printer)


#PrinterクラスはDeviceクラスを継承し、プリンター特有の機能（容量や印刷ページ数など）を追加
class Printer(Device):

    #Deviceクラスの初期化に加え、プリンターの容量（capacity）と、印刷可能な残りページ数（remaining_pages）を初期化
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        # self.name = name
        # self.connected_by = connected_by
        # self.connected = True
        self.capacity = capacity
        self.remaining_pages = capacity
    
    #親クラスの__str__メソッドを拡張し、残りページ数を表示
    def __str__(self):
        return f"{super().__str__()}({self.remaining_pages} pages remaining)"
    
    #指定したページ数を印刷,プリンターが接続されていない場合、警告メッセージ,印刷後、remaining_pagesを更新
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20) # Device 'Printer' (USB)
print(printer) # Printing 20 pages
printer.disconnect() # Device 'Printer' (USB) (480 pages remaining)
printer.print(30) # Your printer is not connected