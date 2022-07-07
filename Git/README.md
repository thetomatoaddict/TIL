# Git



## 정의

분산형 버전 관리 시스템



## 명령어

- $ git init

  로컬 저장소 생성하기	

  

- $ git add <파일명>\

  커밋할 파일들을 staged 상태로 변경	

  

- $ git commit -m '<커밋메시지>'

  커밋 (버전 기록)	

  

- $ git status

  untracked, unmodified, modified, staged 상태 확인
  
  

- $ git log

  커밋 기록 확인
  
  

- $ git push <원격저장소이름> <브랜치 이름>

  커밋한 버전을 원격저장소(github)에 푸쉬
  
  
  
  
- $ git clone <원격저장소 주소>

  원격저장소를 복제하여 모든 버전을 가져옴(.git폴더 포함).
  로컬에서 새로운 프로젝트를 시작할 때는 git init / 원격에 있는 프로젝트를 시작할 때는 git clone
  
  
  

- $ git pull <원격저장소이름> <브랜치 이름>

  원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함
  프로젝트 개발 중 다른 사람 커밋 받아올 때.
  
  
  

- $ git push <원격저장소이름> <브랜치 이름>

  커밋한 버전을 원격저장소(github)에 푸쉬
  
  
  

- $ git remote -v

  추가되어있는 원격 저장소 정보 확인
  
  
  

- $ git remote add <원격저장소 이름> <url>

  원격 저장소 추가 (이름은 일반적으로 origin)
  
  
  

- $ git remote rm <원격저장소 이름>

  원격저장소 삭제
  
  
  

- $ git push <원격저장소이름> <브랜치 이름>

  커밋한 버전을 원격저장소(github)에 푸쉬
