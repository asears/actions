# actions

Github Actions reusable templates

## General Pattern

Templates require workflow_call event tracking.

```yaml
on:
  workflow_call:
    inputs:
      config-path:
        required: true
        type: string
    secrets:
      envPAT:
        required: true
```

## lint-rust

Lint rust code.

https://github.com/asears/waltz/tree/feature/ciupdate/.github/workflows

## scan-secrets

Scan secrets with Trufflehog.

Microsoft also provides a DevSecops action.

https://github.com/microsoft/security-devops-action

## Resources

<https://docs.github.com/en/actions/using-workflows/reusing-workflows>
