## 실행환경

- C++, Python을 사용함
- vscode에서 실행 및 디버깅을 모두 수행
- ctrl + shift + x 로 작업실행을 키 바인딩 하면 사용하기 편하다.
- 실행문은 task.json에 작성하면 되고, 규칙은 vscode doc을 참고
- ctrl + shift + d 로 디버그모드 진입을 설정한다. (이건 아마 vscode 디폴트)
- 디버그 작업도 정의해둬야 하는데 그건 왼쪽 상단의 구성 추가에서 해도됨
- 혹은 launch.json에서 정의해줘도 된다.
- C++ 에서 배열이나 벡터 구조를 편하게 보려면 어떤 특수한 mingw gcc를 써야한다.(구글링해서 구함)
- 안쓰면 메모리 주소만 나옴
- 정형화된 코드는 매크로로 만들자, 참고[https://musma.github.io/2019/08/12/vscode-code-snippets.html]
