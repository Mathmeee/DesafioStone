# Api TimeNow

### Esta api esta rodanddo atualmente em uma ec2, exposta no endereço: http://100.25.181.190:5000/

## Build

### Para fazer o build da imagem usando o dockerfile use o seguinte comando: "docker build -t rest-time-new ."

## Deploy
 
### Para fazer o deploy no docker use o seguinte comando: "docker run -d -p 5000:5000 rest-time-new"

## Observability

### para fazer o monitoramento do container docker irei utilizar datadog

para  rodar datadog fiz as seguintes etapas:

Ir no site deles e criar uma conta.

Após criar a conta ele selecione o docker agent, ele irá fornecer um comando docker. 

instalei o datadog agent no docker com o comando fornecido. 

docker run -d --name dd-agent -v /var/run/docker.sock:/var/run/docker.sock:ro -v /proc/:/host/proc/:ro -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro -e DD_API_KEY=APIKEYHERE -e DD_SITE="us5.datadoghq.com" gcr.io/datadoghq/agent:7

Após isso, clique em finalizar e ele irá redirecionar para o painel do datadog.

Seria possível criar um dashboard bem detalhado do container, mas o datadog já fornece um dashboard default do docker, para acessa-lo vá em dashboards e clique no dashboard "Docker - Overview"

Url publica da api: http://100.25.181.190:5000/
