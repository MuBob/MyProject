import xlwt as xlwt


class FileOutput:
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_file(self):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('sheet 1')
        sheet.write(0, 0, 'url')  # 第0行第一列写入内容
        sheet.write(0, 1, 'title')  # 第0行第一列写入内容
        sheet.write(0, 2, 'summary')  # 第0行第一列写入内容
        row = 1
        for data in self.datas:
            sheet.write(row, 0, data["url"])
            sheet.write(row, 1, data["title"])
            sheet.write(row, 2, data["summary"])
            row += 1

        wbk.save('test.xls')
        # with open(file='out.xls', mode='w', encoding='utf-8') as f_out:
        #     for data in self.datas:
        #         f_out.write('url=%s\n\t' % data["url"])
        #         f_out.write('title=%s\n\t' % data["title"])
        #         f_out.write('summary=%s\n\n\n' % data["summary"])
