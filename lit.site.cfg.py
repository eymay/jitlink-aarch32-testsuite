import os

config.my_src_root = os.getcwd()

lit_config.load_config(
        config, os.path.join(config.my_src_root, "test/lit.cfg.py"))
