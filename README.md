## 실행환경

- C++, Python, Java를 사용

### C++ & Python
- vscode에서 실행 및 디버깅을 모두 수행
- ctrl + shift + x 로 작업실행을 키 바인딩 하면 사용하기 편하다.
- 실행문은 task.json에 작성하면 되고, 규칙은 vscode doc을 참고하거나 본 레포지토리에 올라온 task.json을 참고해도 된다.
- 컴파일러 경로등은 다를 수 있으니 주의
- ctrl + shift + d 로 디버그모드 진입을 설정한다. (이건 아마 vscode 디폴트)
- 디버그 작업도 정의해둬야 하는데 그건 왼쪽 상단의 구성 추가에서 해도됨
- 혹은 launch.json에서 정의해줘도 된다.
- C++ 에서 배열이나 벡터 구조를 편하게 보려면 특수한 mingw gcc를 써야한다.(구글링하면 소스포지가 나온다.)
- 기본 gcc로 디버깅하면 메모리 주소만 나옴

### Java
- Java 8을 기준으로 작성한다.
- adopt-openjdk-1.8을 사용한다. JVM 버전은 hotsopt 1.8이다.
- `<문제번호>.java` 형태로 파일명을 작성하는 것에 주의(클래스 명은 Main임)
