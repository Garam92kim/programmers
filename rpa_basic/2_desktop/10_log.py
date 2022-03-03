import logging
from datetime import datetime

# # debug < info < warning < error < critical
# logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s") # DEBUG LEV 이상 모든 lOG를 찍음
# logging.debug("아 이거 누가 짠거야~~~~")
# logging.info("자동화 수행 준비")
# logging.warn("이 스크립트는오래 되었습니다.~ 문제가 있을 수 있습니다")
# logging.error("error가 발생,")
# logging.critical("복구가 불가능한 심각한 문제가 발생")

# 터미널과 파일에 함께 로그 남기기
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 lev 설정
logger.setLevel(logging.DEBUG)


# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("ㄹ그를 남겨보는 테스트를 진행")