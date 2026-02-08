# CI/CD 與分支／Tag 設計

## 分支策略

| 分支 | 用途 |
|------|------|
| **dev** | 整合分支。feature 開 PR 合到 dev，CI 在 push/PR 時跑測試、覆蓋率、打 semver tag。 |
| **main**（選用） | 正式／對外分支。可只在 release 時從 dev merge 進來，或不用 main、只靠 tag 做 release。 |

- 日常開發：`feature/xxx` → PR → **dev**
- 要對外釋出時：由 **dev 通過 CI 後自動打 tag**，或手動打 tag，觸發 CD 建 wheel 與 GitHub Release

## Tag 策略

| Tag 格式 | 意義 | 誰建立 |
|----------|------|--------|
| **v1.0.0**（semver） | 正式 release。觸發 CD：建 .whl、建立 GitHub Release、上傳 .whl。 | ci-dev 通過後自動（compute-next-version）或手動 |
| **dev-123**（選用） | 僅標記某次 dev 的 CI run，不觸發 release。 | ci-dev 可選 |

- **v*** 一律視為 release tag：push 任一 `v*` 會觸發 `cd-release.yml` 建 wheel 並發 Release。
- 版本號規則：0.0.0 → 0.0.1 → … → 0.0.99 → 0.1.0 → … → 0.99.99 → 1.0.0（見 `.github/actions/compute-next-version`）。

## Workflow 分工

| 檔案 | 觸發 | 做的事 |
|------|------|--------|
| **ci-dev.yml** | push / PR 到 **dev** | 測試、覆蓋率、上傳測試報告 artifact；通過後打 **v* tag**（可選）。 |
| **cd-release.yml** | push **tag** 符合 **v*** | 用 tag 版本號建 Python .whl、建立 GitHub Release、上傳 .whl 為 Release asset。 |

## 流程概覽

```
feature/xxx → PR → dev
                     ↓
              CI (test, coverage)
                     ↓ (pass)
              打 tag v0.0.x 並 push
                     ↓
              CD (build wheel, GitHub Release)
                     ↓
              Release 頁面出現 v0.0.x，可下載 .whl
```

若不想每次 dev 通過都發 release，可關閉 ci-dev 裡的自動打 tag，改為**手動**在 GitHub 建立 tag（或從 main merge 後手動打 tag），一樣會觸發 cd-release。

## 若要多一個 main 當「正式分支」

1. 平常只在 **dev** 開發與跑 CI。
2. 要 release 時：從 dev merge 到 main（或 PR main ← dev），在 **main** 上打 tag v* 並 push。
3. 把 **cd-release.yml** 維持「觸發條件：push tag v*」即可，不需改成分支。

這樣 main 只會是「已 release 的 commit」，tag 一定打在 main 上；dev 則可關閉自動打 tag，改為手動在 main 打 tag 再 push。
