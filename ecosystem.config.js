module.exports = {
  apps: [
    {
      name: "django-backend",
      script: "manage.py",
      args: ["runserver 8000"],
      exec_mode: "cluster",
      instances: "max",
      interpreter: "python3",
    },
  ],
};
