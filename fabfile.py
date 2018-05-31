from invoke import task


# Deploy with:
# $ fab -H root@konradhalas.pl --prompt-for-passphrase deploy

@task
def deploy(c):
    with c.cd('/home/apps/apps/konradhalas.pl/'):
        c.run('git -C repo pull')
        c.run('docker-compose -p mysite -f repo/containers/docker-compose.yml up -d --no-deps --build app')
