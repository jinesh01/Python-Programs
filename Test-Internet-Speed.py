import speedtest as st
def get_new_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()
    download = speed_test.download()
    upload = speed_test.upload()
    download_mbs = round(download /(10**6),2)
    print("Download Speed {} ".format(download_mbs))
    ipload_mbs = round(download /(10**6),2)
    print("Upload Speed {} ".format(upload_mbs))
new_speeds = get_new_speeds()
