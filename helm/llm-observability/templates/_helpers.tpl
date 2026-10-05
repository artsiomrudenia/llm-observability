{{- define "llm-observability.fullname" -}}
{{- default "llm-observability" .Release.Name -}}
{{- end -}}
