# developer guide
```mermaid
stateDiagram-v2
    [*] --> Input
    Input --> lexer
    asn --> lexer
    lexer --> ast
    ast --> execute