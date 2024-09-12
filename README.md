graph TD;
    A[Planificación y Diseño] --> B[Desarrollo]
    B --> C[Testing]
    C --> D[Despliegue en Producción]
    D --> E[Monitorización y Logs]
    E --> F[Escalabilidad]
    F --> G[Mantenimiento Continuo]

    A --> |Lucidchart, Draw.io| A1[Diseño de arquitectura]
    A --> |Trello, Jira| A2[Gestión de tareas]

    B --> |Docker Compose| B1[Contenerización de servicios]
    B --> |Git/GitHub| B2[Control de versiones]
    B --> |Visual Studio Code| B3[Desarrollo]

    C --> |Jenkins, GitLab CI/CD| C1[Automatización de pruebas]
    C --> |Mocha/Jest, JUnit| C2[Pruebas unitarias]
    C --> |Selenium| C3[Pruebas end-to-end]

    D --> |Terraform| D1[Aprovisionar infraestructura]
    D --> |Kubernetes| D2[Orquestación de contenedores]
    D --> |Certbot, NGINX| D3[Configurar HTTPS y balanceo de carga]

    E --> |Prometheus| E1[Monitorización de métricas]
    E --> |Grafana| E2[Visualización de métricas]
    E --> |Fluentd, ELK Stack| E3[Gestión de logs]

    F --> |Kubernetes Autoscaler| F1[Autoescalado de contenedores]
    F --> |Prometheus| F2[Monitorización de escalabilidad]

    G --> |Terraform| G1[Actualización de infraestructura]
    G --> |Helm| G2[Actualización de aplicaciones]
