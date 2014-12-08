__author__ = 'moisessiles'

if __name__ == "__main__":
    config = {}
    execfile("config.cfg", config)
    # python 3: exec(open("example.conf").read(), config)

    print config["url"]