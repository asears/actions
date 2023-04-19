# actions

Github Actions reusable templates

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

## Resources

<https://docs.github.com/en/actions/using-workflows/reusing-workflows>
