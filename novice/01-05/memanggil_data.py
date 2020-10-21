import xml.dom.minidom as minidom

def main():
    # gunakan fungsi parse() untuk me-load xml ke memori 
    # dan melakukan parsing
    doc = minidom.parse("01-05/data.xml")

    # Cetak isi doc dan tag pertamanya
    print('doc.nodeName')
    print('doc.firstChild.tagName')

    nama = doc.getElementsByTagName("nama")[0].firstChild.data
    alamat = doc.getElementsByTagName("alamat")[0].firstChild.data
    jurusan = doc.getElementsByTagName("jurusan")[0].firstChild.data
    list_hobi = doc.getElementsByTagName("hobi")

    print ("Nama: {}\nAlamat: {}\nJurusan: {}\n".format(nama, alamat, jurusan))

    print ("Memiliki {} hobi:".format(len(list_hobi)))

    for hobi in list_hobi:
        print ("alamat", hobi.getAttribute("nama"))


if __name__ == "__main__":
    main()
