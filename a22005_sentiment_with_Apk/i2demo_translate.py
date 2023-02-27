import argostranslate.package, argostranslate.translate

from_code = "zh"
to_code = "en"

# Download and install Argos Translate package
available_packages = argostranslate.package.get_available_packages()
print('available_packages=', available_packages)
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]
print('2 available_package=', available_package)
download_path = available_package.download()
print('download_path=', download_path)
argostranslate.package.install_from_path(download_path)

# Translate
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = list(filter(
        lambda x: x.code == from_code,
        installed_languages))[0]
to_lang = list(filter(
        lambda x: x.code == to_code,
        installed_languages))[0]
translation = from_lang.get_translation(to_lang)
target = "我觉得说得评论说得对。世界，你好！"
translatedText = translation.translate(target)
print(target,'->', translatedText)