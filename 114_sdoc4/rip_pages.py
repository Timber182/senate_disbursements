import os

start_page = 17
end_page = 2073

# this is including compensation to members. Is that ok? 


page_range = range(start_page, end_page+1)
for page_number in page_range:
    output_filename = "pages/layout_%s.txt" % (page_number)
    layout_cmd = "pdftotext -f %s -l %s -layout GPO-CDOC-114sdoc4.pdf %s" % (page_number, page_number, output_filename)
    print layout_cmd
    result = os.popen(layout_cmd).read()
    print result

