import os
import json
import colorama as c

INPUT_FILE = "./channels.json"
OUTPUT_FILE = "./BUPT_IPTV.m3u"


def main():
    # input file judgement
    if not os.path.exists(INPUT_FILE):
        print(c.Fore.RED + c.Style.BRIGHT + "INPUT FILE MISSING!")
        exit(1)

    # load in the channels_list
    channels_list = []
    with open(INPUT_FILE, "r+", encoding='utf-8') as f_in:
        channels_list = json.load(f_in)["channels"]
    print(c.Fore.GREEN + "Loading in channels done!")

    # write in m3u file
    with open(OUTPUT_FILE, 'w+', encoding='utf-8') as f_out:
        print(c.Fore.GREEN + "Processing:")
        f_out.writelines("#EXTM3U\n")

        for channel in channels_list:  # each channel
            f_out.writelines("#EXTINF: -1, {}\n".format(channel["title"]))
            f_out.writelines(channel["url"] + "\n")
            print(c.Fore.BLUE + "  " + channel["title"] + " : " + channel["url"])

    print(c.Fore.GREEN + "M3U file creating done!")


if __name__ == '__main__':
    main()
