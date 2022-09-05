import pip


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


if __name__ == '__main__':
    install('html2text')
    install('Cython')
    install('kss==2.5.1')
    install('tqdm')
    install('attrdict')
    install('ray')
    print("done")