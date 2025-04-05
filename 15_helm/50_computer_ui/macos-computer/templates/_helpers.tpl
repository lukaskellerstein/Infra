{{- define "proxy.name" -}}
{{ .Values.computerName }}-proxy
{{- end }}

{{- define "proxy.route" -}}
/{{ .Values.computerName }}
{{- end }}

{{- define "proxy.vnc_host" -}}
"{{ .Values.computerName }}"
{{- end }}