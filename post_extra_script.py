import os
Import("env")

def after_build(source, target, env):
    print("Calling aggregate shell script")
    os.system("./aggregate_bin.sh")

env.AddPostAction("buildprog", after_build)
