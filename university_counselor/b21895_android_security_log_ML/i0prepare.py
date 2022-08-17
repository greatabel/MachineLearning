import os
import shutil

def main():
  msources = [
      "/CICInvesAndMal2019/Adware",
      "/CICInvesAndMal2019/PremiumSMS",
      "/CICInvesAndMal2019/SMS",
      "/CICInvesAndMal2019/Ransomware",
      "/CICInvesAndMal2019/Scareware",
  ]

  for s in msources:
      for root, dirs, files in os.walk(s):
          for file in files:
              if file.endswith(".apk"):
                  print(file)
                  shutil.copy(os.path.join(root, file), "/CICInvesAndMal2019/malign/")

  bsources = ["/CICInvesAndMal2019/Benign_2016", "/CICInvesAndMal2019/Benign_2017"]
  for p in bsources:
      for root, dirs, files in os.walk(p):
          for file in files:
              if file.endswith(".apk"):
                  print(file)
                  shutil.copy(os.path.join(root, file), "/CICInvesAndMal2019/benign/")
                  os.remove(os.path.join(root, file))

  print('classify finish')


if __name__ == "__main__":
  main()