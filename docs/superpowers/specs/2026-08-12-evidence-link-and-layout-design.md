# 평가 근거 링크 및 무충돌 배치 설계

## 목표

31개 평가 문항을 문구의 원자 조건별로 증명하는 근거 링크를 제공한다. 모든 링크는
`wilderif/codyssey-b7-1` 저장소 `main` 브랜치의 실제 파일과 정확한 단일 행 또는 연속 행 범위를
가리킨다. 근거 숫자, 분 단위 잠금 해제 숫자, 함정 숫자는 화면에서 서로 겹치지 않는다.

## 링크 선정 원칙

1. 문항에 `README.md에`가 명시된 조건은 반드시 `README.md` 근거를 사용한다.
2. 구현 여부를 묻는 조건은 실제 template, router, service, repository, model 등 구현 파일을 사용한다.
3. `문서화`만 요구하는 조건은 해당 책임을 가진 `docs/spec` 문서를 사용할 수 있다.
4. `README.md 또는 API 문서`처럼 대안이 명시된 경우 정확한 근거가 있으면 README를 우선한다.
5. 하나의 연속된 근거는 `#L시작-L끝`, 한 행 근거는 `#L행`으로 연결한다.
6. 서로 떨어진 근거 블록은 같은 평가 숫자를 여러 번 생성한다.
7. 링크 URL은 예외 없이 `https://github.com/wilderif/codyssey-b7-1/blob/main/<path>#L...` 형식이다.
8. PR·commit 페이지로 직접 이동하지 않는다. 24번과 31번은 PR·commit 링크를 포함한 README의
   정확한 행 범위를 가리킨다.

## 문항별 근거 매핑

| 문항 | 정확한 `main` 근거 블록 |
| ---: | --- |
| 1 | `README.md#L7`, `README.md#L9` |
| 2 | `README.md#L97-L125`, `README.md#L131` |
| 3 | `README.md#L190-L204`, `README.md#L212-L219`, `README.md#L221-L234`, `README.md#L236-L260` |
| 4 | `README.md#L306`, `README.md#L308-L333`, `README.md#L335-L349` |
| 5 | `README.md#L355-L365`, `README.md#L367-L377`, `README.md#L379-L383` |
| 6 | `README.md#L389-L397` |
| 7 | `app/ui/templates/signup.html#L8-L21`, `app/ui/templates/_auth_form.html#L12-L51`, `README.md#L172-L174`, `app/ui/router.py#L63-L89`, `app/auth/service.py#L72-L101` |
| 8 | `app/main.py#L60-L66`, `app/auth/dependencies.py#L26-L32`, `README.md#L176`, `README.md#L178-L184` |
| 9 | `app/auth/dependencies.py#L50-L69`, `app/chat/router.py#L41-L58`, `app/chat/router.py#L162-L172`, `README.md#L168` |
| 10 | `app/ui/templates/chat.html#L28-L60`, `app/ui/templates/chat.html#L68-L103`, `app/ui/templates/chat.html#L105-L123`, `app/ui/static/chat.js#L197-L205`, `app/ui/static/chat.js#L207-L239`, `app/ui/router.py#L144-L168` |
| 11 | `app/chat/service.py#L97-L113`, `app/chat/openai_client.py#L26-L37`, `docs/spec/ai/AI.md#L9-L14`, `docs/spec/ai/AI.md#L16-L24`, `docs/spec/ai/AI.md#L38-L54` |
| 12 | `app/chat/models.py#L49-L97`, `app/chat/repository.py#L141-L195`, `app/chat/service.py#L143-L158`, `docs/spec/db/DB.md#L145-L172` |
| 13 | `app/ui/router.py#L144-L168`, `app/chat/service.py#L226-L257`, `app/chat/router.py#L81-L128`, `app/admin/router.py#L24-L45`, `app/ui/templates/admin_logs.html#L8-L86`, `docs/spec/api/API.md#L76-L105` |
| 14 | `app/core/config.py#L38-L40`, `app/chat/openai_client.py#L26-L37`, `app/chat/openai_client.py#L48-L65`, `docs/spec/ai/AI.md#L56-L73` |
| 15 | `app/chat/router.py#L71-L74`, `app/chat/router.py#L162-L174`, `app/chat/i18n.py#L7-L34`, `docs/spec/api/API.md#L174-L207` |
| 16 | `app/chat/schemas.py#L13-L31`, `app/chat/service.py#L260-L266`, `app/ui/static/chat.js#L135-L148`, `README.md#L208-L210`, `README.md#L290-L300` |
| 17 | `app/chat/schemas.py#L13-L60`, `app/chat/router.py#L34-L78`, `app/chat/service.py#L67-L164`, `app/chat/openai_client.py#L19-L65`, `app/chat/repository.py#L13-L65` |
| 18 | `README.md#L136-L151`, `README.md#L154-L162`, `app/ui/router.py#L107-L141` |
| 19 | `app/chat/schemas.py#L13-L60`, `app/chat/router.py#L28-L34`, `docs/spec/api/API.md#L231-L286` |
| 20 | `app/main.py#L60-L66`, `app/auth/dependencies.py#L50-L70`, `app/chat/router.py#L41-L58`, `app/chat/router.py#L81-L89`, `app/chat/router.py#L101-L115` |
| 21 | `app/chat/models.py#L49-L97`, `app/chat/repository.py#L13-L65`, `app/chat/repository.py#L68-L138`, `app/chat/repository.py#L198-L241`, `app/auth/repository.py#L11-L47` |
| 22 | `app/core/config.py#L13-L40` |
| 23 | `.env.example#L1-L6`, `.gitignore#L14-L18` |
| 24 | `README.md#L401-L410` |
| 25 | `README.md#L188-L204`, `README.md#L262-L288`, `app/chat/router.py#L81-L128` |
| 26 | `README.md#L166-L170` |
| 27 | `README.md#L48-L58`, `app/core/config.py#L30-L32`, `app/chat/openai_client.py#L48-L65` |
| 28 | `app/chat/openai_client.py#L26-L37`, `app/chat/openai_client.py#L48-L65`, `app/chat/router.py#L69-L74`, `docs/spec/ai/AI.md#L56-L73` |
| 29 | `README.md#L353-L383`, `README.md#L385-L387` |
| 30 | `app/chat/models.py#L49-L97`, `app/chat/router.py#L61-L67`, `app/chat/service.py#L92-L162`, `app/chat/repository.py#L141-L195`, `docs/spec/db/DB.md#L48-L65` |
| 31 | `README.md#L412-L425` |

총 106개 근거 블록이다. 최초 설계 이후 PASS 평가서가 실제 판정 근거로 인용한 코드 중 기존 범위에
없던 10개 흐름을 같은 평가 번호에 추가했다.

## 숫자 밀도

- 기존 근거 링크: 62개
- 최초 변경 근거 링크: 96개
- PASS 평가 반영 근거 링크: 106개
- 최종 증가량: 44개
- 기존 함정 숫자: 실수형 48개 + 정수형 110개 = 158개
- 변경 함정 숫자 상한: 실수형 48개 + 정수형 66개 = 114개

근거 숫자 증가량만큼 정수형 함정 숫자를 44개 줄여 기본 장면의 전체 숫자 상한을 유지한다.
좁은 화면에서 114개를 모두 무충돌로 배치할 공간이 없으면 함정 숫자만 추가로 생략한다. 근거 숫자와
잠금 해제 숫자는 생략하지 않는다.

## 무충돌 배치

1. 잠금 해제 숫자와 근거 숫자를 필수 요소로 먼저 배치한다.
2. 근거 숫자는 기존처럼 평가 번호에 대응하는 31개 세로 열을 유지한다.
3. 후보 위치에 요소를 놓은 뒤 회전이 반영된 `getBoundingClientRect()`를 측정한다.
4. 화면 경계를 벗어나거나 기존 사각형과 안전 간격을 두고 충돌하면 후보를 폐기한다.
5. 필수 요소가 모두 들어갈 때까지 후보 위치를 탐색하며, 필요한 경우 숫자 글꼴 크기를 단계적으로
   줄여 다시 배치한다.
6. 필수 요소 배치 후 함정 숫자를 같은 충돌 검사로 채운다. 공간이 없으면 해당 함정 숫자를 DOM에서
   제거한다.
7. 분이 바뀌거나 `ResizeObserver`가 화면 크기 변경을 감지하면 전체 배치를 다시 계산한다.
8. 질감 배경 이미지에는 숫자가 없으므로 충돌 검사 대상에서 제외한다.

## 검증

1. 1부터 31까지 모든 문항이 존재하고 총 근거 블록이 106개인지 검사한다.
2. 모든 링크가 `blob/main`과 유효한 `#L...` 또는 `#L...-L...` 앵커를 사용하는지 검사한다.
3. 대상 저장소 최신 `main`에서 모든 파일과 행 범위가 실제로 존재하는지 검사한다.
4. README 명시 문항의 README 근거 누락을 검사하며, 특히 3번의 네 링크가 모두 README인지 검사한다.
5. 브라우저 크기별로 모든 렌더링 숫자의 회전 후 경계가 서로 겹치지 않는지 검사한다.
6. 잠금 해제, 링크 한 번 사용 후 재잠금, 새 탭 열기 동작이 유지되는지 검사한다.
